// Pixel-art agent avatars.
//
// The art is drawn in art/generate.py and saved as animated GIFs, one per
// avatar and state: art/<avatar>-<state>.gif. The app plays GIFs natively,
// so the script never has to redraw to animate them. The generator also
// writes art/avatars.js, the list of every avatar, most distinct first.

import { div, image } from "gpui-kit";
import { shared, setShared, spaces, agents, panes } from "herdr";
import { AVATARS, LOOKS, ACCESSORIES } from "./art/avatars.js";

export { AVATARS };

const BY_ID = new Map(AVATARS.map((a) => [a.id, a]));
const STATES = new Set(["working", "blocked", "done", "idle"]);

// Any id we don't know (say, from an older version) falls back to the first.
const find = (id) => BY_ID.get(id) ?? AVATARS[0];

// The GIFs are 28x26 art pixels at 4x. Shown at 2 logical px per art pixel,
// a 2x screen draws each art pixel as exactly 4x4 device pixels: crisp.
const ART_W = 28;
const ART_H = 26;

// An avatar (by id) in a status. Unknown statuses fall back to idle.
export function avatar(status, id, scale = 2) {
  const s = STATES.has(status) ? status : "idle";
  return image(`mods/retro-sidebar/art/${find(id).id}-${s}.gif`)
    .w(ART_W * scale)
    .h(ART_H * scale)
    .flex_none();
}

// The habitat drawn behind an avatar: its character's scene, at night while
// the agent sleeps. Habitats are 40x32 art pixels, shown at the same scale.
const HAB_W = 40;
const HAB_H = 32;
// Where the avatar stands inside the habitat, in art pixels.
const STAND_X = 6;
const STAND_Y = 5;

export function habitat(status, id, scale = 2) {
  const time = status === "idle" ? "night" : "day";
  return div()
    .relative()
    .flex_none()
    .w(HAB_W * scale)
    .h(HAB_H * scale)
    .overflow_hidden()
    .child(image(`mods/retro-sidebar/art/habitat-${find(id).character}-${time}.png`).absolute().inset_0().size_full())
    .child(div().absolute().left(STAND_X * scale).top(STAND_Y * scale).child(avatar(status, id, scale)));
}

// Who is who. A space has a look (character + color, like "sparky-lilac"), and
// each agent in that space wears an accessory on top of it, so the look says
// which space an agent is in and the accessory says which agent it is. Both are
// kept in shared state so they never change and every mod shows the same ones.
// Only this file reads or writes these keys.
const LOOK_KEY = "retro.looks"; // space id -> look
const ACCESSORY_KEY = "retro.accessories"; // agent pane -> accessory
// Before looks existed, a space's avatar was stored here (space id -> "look-accessory").
// It is read only, so existing spaces keep the creature they had.
const LEGACY_KEY = "retro.avatars";

const isLook = (look) => LOOKS.includes(look);

// The look a space had before looks existed, or null.
function legacyLook(spaceId) {
  const old = (shared(LEGACY_KEY) ?? {})[spaceId];
  if (typeof old !== "string") return null;
  const look = old.slice(0, old.lastIndexOf("-"));
  return isLook(look) ? look : null;
}

// The look every open space uses, counting spaces not yet migrated.
function lookUses(looks) {
  const uses = new Map(LOOKS.map((look) => [look, 0]));
  for (const s of spaces()) {
    const look = isLook(looks[s.id]) ? looks[s.id] : legacyLook(s.id);
    if (uses.has(look)) uses.set(look, uses.get(look) + 1);
  }
  return uses;
}

// A space's look. A new space gets the least used look among open spaces,
// earliest in LOOKS order on ties, so the most distinct ones go first. A
// closed space keeps its entry (if it comes back, so does its look).
export function lookFor(spaceId) {
  if (!spaceId) return LOOKS[0];
  const looks = shared(LOOK_KEY) ?? {};
  if (isLook(looks[spaceId])) return looks[spaceId];
  const uses = lookUses(looks);
  const fewest = Math.min(...uses.values());
  const look = legacyLook(spaceId) ?? LOOKS.find((l) => uses.get(l) === fewest);
  setShared(LOOK_KEY, { ...looks, [spaceId]: look });
  return look;
}

// A space's own avatar: its look with the plain accessory.
export function spaceAvatar(spaceId) {
  return `${lookFor(spaceId)}-plain`;
}

// An agent's accessory, keyed by its pane. A new agent adopts the accessory it
// wore under its terminal address (the old key) when no other live agent in its
// space wears it. Otherwise it gets the first accessory no other live agent in
// its space wears, in ACCESSORIES order. When all are worn, the least worn one
// repeats. Each new assignment writes once and drops keys that are not live panes.
function accessoryFor(agent) {
  const worn = shared(ACCESSORY_KEY) ?? {};
  if (ACCESSORIES.includes(worn[agent.pane])) return worn[agent.pane];
  const live = agents();
  const uses = new Map(ACCESSORIES.map((acc) => [acc, 0]));
  for (const other of live) {
    if (other.space !== agent.space || other.pane === agent.pane) continue;
    const acc = worn[other.pane];
    if (uses.has(acc)) uses.set(acc, uses.get(acc) + 1);
  }
  const legacy = worn[agent.address];
  const adopt = ACCESSORIES.includes(legacy) && uses.get(legacy) === 0;
  const fewest = Math.min(...uses.values());
  const pick = adopt ? legacy : ACCESSORIES.find((acc) => uses.get(acc) === fewest);
  const livePanes = new Set([...panes().map((p) => p.pane), ...live.map((a) => a.pane)]);
  const kept = Object.fromEntries(Object.entries(worn).filter(([key]) => livePanes.has(key)));
  setShared(ACCESSORY_KEY, { ...kept, [agent.pane]: pick });
  return pick;
}

// An agent's avatar (agent from agents()): its space's look, with its accessory.
export function agentAvatar(agent) {
  return `${lookFor(agent.space)}-${accessoryFor(agent)}`;
}
