(function () {
    window.addEventListener('resize', event => {
        showDisplaySize();
    }, true);

    selectAll('botcity')
})();

function selectAll(id) {
    const element = document.getElementById(id);
    if (document.body.createTextRange) {
        const range = document.body.createTextRange();
        range.moveToElementText(element);
        range.select();
    } else if (window.getSelection) {
        const selection = window.getSelection();
        const range = document.createRange();
        range.selectNodeContents(element);
        selection.removeAllRanges();
        selection.addRange(range);
    } else {
        console.warn("Could not select text in node: Unsupported browser.");
    }
}

function showDisplaySize() {
    document.getElementById('screen-size').innerText = `${window.screen.width}x${window.screen.height}`;
    document.getElementById('page-size').innerText = `${window.innerWidth}x${window.innerHeight}`;
    document.getElementById('window-size').innerText = `${window.outerWidth}x${window.outerHeight}`;
    document.getElementById('is-maximized').innerText = screen.availWidth - window.innerWidth === 0;
}
