import { View } from "gpui-kit";
import { props } from "herdr";
import Agents from "./agents.js";
import Spaces from "./spaces.js";

// One mod, two panels: the layout block's props.role picks which.
// Overlays opened by the agents code pass no role, so they get Agents.
export default class RetroSidebar extends View {
  init(p, cx) {
    this.inner = props()?.role === "spaces" ? new Spaces() : new Agents();
    this.inner.init?.(p, cx);
  }
  update(p) {
    this.inner?.update?.(p);
  }
  render(cx) {
    return this.inner.render(cx);
  }
  async close(cx) {
    await this.inner?.close?.(cx);
  }
}
