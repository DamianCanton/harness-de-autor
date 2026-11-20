// One agent as a card: its avatar in its habitat on the left, and on the
// right what it is doing, which space it belongs to and for how long.

import { div } from "gpui-kit";
import { v_flex, h_flex } from "gpui-base";
import { habitat } from "./sprites.js";

const LABEL = { working: "WORKING", blocked: "NEEDS YOU", done: "DONE", idle: "IDLE" };

// The status as a small pixel-style tag, in the theme's color for it.
function tag(t, status) {
  const color = t[status] ?? t.dim;
  return div()
    .flex_none()
    .px(5)
    .h(16)
    .flex()
    .items_center()
    .rounded(2)
    .bg(color + "26")
    .border(1)
    .border_color(color + "66")
    .font_family("JetBrains Mono")
    .text_size(9.5)
    .font_bold()
    .text_color(color)
    .child(LABEL[status] ?? String(status).toUpperCase());
}

// card(t, {id, status, avatar, name, detail, time, focused, extras, onClick, onHover})
// `extras` is an element shown next to the time (pin, fold, machine).
export function card(t, a) {
  const asleep = a.status === "idle" && !a.focused;
  return h_flex()
    .id(a.id)
    .flex_none()
    .p(5)
    .gap(9)
    .items_center()
    .rounded(6)
    .bg(t.surface)
    .border(2)
    .border_color(a.focused ? t.accent : t.border)
    .cursor_pointer()
    .hover((s) => s.border_color(a.focused ? t.accent : t.input))
    .when(Boolean(a.onClick), (el) => el.on_click(a.onClick))
    .when(Boolean(a.onHover), (el) => el.on_hover(a.onHover))
    .child(div().rounded(3).overflow_hidden().border(1).border_color(t.border).child(habitat(a.status, a.avatar)))
    .child(
      v_flex()
        .flex_1()
        .min_w(0)
        .gap(4)
        .child(
          h_flex()
            .h(18)
            .gap(6)
            .items_center()
            .child(tag(t, a.status))
            .child(div().flex_1())
            .when(Boolean(a.extras), (el) => el.child(a.extras))
            .when(Boolean(a.time), (el) => el.child(div().text_size(10.5).text_color(t.dim).child(a.time))),
        )
        .child(div().truncate().text_size(13).font_semibold().text_color(asleep ? t.muted : t.foreground).child(a.name))
        .when(Boolean(a.detail), (el) => el.child(div().truncate().text_size(11).text_color(t.dim).child(a.detail))),
    );
}
