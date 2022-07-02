from rich.align import Align
from rich.console import RenderableType
from rich.text import Text
from rich.tree import Tree
from termtyper.events.events import BarThemeChange, ParaSizeChange, TimeoutChange
from termtyper.ui.widgets.menu import Menu


class SizeMenu(Menu):
    def __init__(self):
        options = ["teensy", "small", "big", "huge"]
        super().__init__(
            "paragraph_size",
            options,
            ParaSizeChange,
            draw_border=True,
            title="How much words can your fingers handle?",
            section="user",
        )


class TimeoutMenu(Menu):
    def __init__(self):
        options = ["15", "30", "60", "120"]
        super().__init__(
            "timeout",
            options,
            TimeoutChange,
            draw_border=True,
            title="How much time can your fingers last?",
            section="user",
        )
    def render(self) -> RenderableType:
        tree = Tree("")
        tree.hide_root = True
        tree.expanded = True
        for index, i in enumerate(self.options):
            label = Text(i.ljust(self._max_len))
            label.append(" seconds")

            if index == self._cursor:
                label.stylize("b green")
                label = Text("> ") + label
            else:
                label = Text("  ") + label

            tree.add(Align.center(label))
        return self.render_panel(tree)


class BarThemeMenu(Menu):
    def __init__(self):
        options = ["minimal", "pacman", "doge", "ballon", "rust"]
        super().__init__(
            "bar_theme",
            options,
            BarThemeChange,
            draw_border=True,
            title="Choose your theme",
            section="theming",
        )
