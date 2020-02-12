$$(function() {
    function show_dialog(title, context) {
        $("div .mdui-container").append("  <div class='mdui-dialog' id='dialog'>" \
            "<div class='mdui-dialog-title'>" + title + "</div>" \
            "<div class='mdui-dialog-content'>" + context + "</div>" \
            "<div class='mdui-dialog-actions'>" \
            "<button class='mdui-btn mdui-ripple' mdui-dialog-confirm>OK</button>" \
            "</div>" \
            "</div>");
    }
    function translate(item) {
        $.post("/translate", {"id": item}, function())
    }
    function set_config(item, value) {
        $.post("/config", {"k": item, "v": value}, function(d, s) {
            if(d != "ok") {
                show_dialog("Error");
            }
        });
    }
})