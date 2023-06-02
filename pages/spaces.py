from pages import chat, files, tasks
import data


spaces = {
    name: {
        "chat": chat.make_tab(),
        "files": files.make_tab(),
        "tasks": tasks.make_tab(),
    }
    for name in data.spaces
}
