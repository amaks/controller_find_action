import sublime, sublime_plugin
# super+shift+6

class ControllerFindActionCommand(sublime_plugin.TextCommand):
  def run(self, edit):

    all_defs      = self.view.find_all(' def ')
    actions       = []

    for d in all_defs:
      line        = self.view.line(d)
      line_text   = self.view.substr(line)
      action_name = line_text.split('def ')[1].strip()
      actions.append(action_name)

    self.actions = actions

    sublime.active_window().show_quick_panel(actions, self.go_to_action)

  def go_to_action(self, index):
    action_def   = self.view.find('def ' + self.actions[index], 0)
    line, column = self.view.rowcol(action_def.begin())
    self.view.run_command("goto_line", {"line": line + 2} )



