function closeSelf(sender) {
    try {
        window.opener.handlePopupResult(sender.getAttribute("src"));
    }
    catch (err) {}
    window.close();
    return false;
}
