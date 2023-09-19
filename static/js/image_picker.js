function closeSelf(sender) {
    try {
        window.opener.focus();
        window.opener.handlePopupResult(sender.getAttribute("src"));
    }
    catch (err) {}
    window.close();
}
