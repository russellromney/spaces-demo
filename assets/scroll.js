// edited from:
// https://stackoverflow.com/a/18614545

var lastMessage = ""

function updateScroll(){
    var chatList = document.getElementById("chat-list")
    if (!chatList) {
        return
    } 
    message = chatList.lastChild.innerHTML
    if (lastMessage != message) {
        var element = document.getElementById("chat-tab")
        lastMessage = message
        element.scrollTop = element.scrollHeight;
    }
}
//once a second ish
setInterval(updateScroll,333);