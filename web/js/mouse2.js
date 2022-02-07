function mouseOverEvent(dataText) {
    elementResult.data = [dataText];
    document.getElementById('element-result').innerText = JSON.stringify(elementResult);
}

function mouseHoldAndReleaseEvent(event, mouseEventType, mouseStatusId) {
    let clickType = '';
    switch (event.button) {
        case 0:
            clickType = `Left${mouseEventType}`;
            break;
        case 1:
            clickType = `Middle${mouseEventType}`;
            break;
        case 2:
            clickType = `Right${mouseEventType}`;
            break;
    }

    document.getElementById(mouseStatusId).innerText = clickType;

    if (elementResult.data[0] === 'mouse-over' || elementResult.data[0] === 'mouse-over2') {
        elementResult.data.shift();
    }

    if (mouseEventType.length <= 2) {
        elementResult.data.push(clickType)
    } else {
        elementResult.data = [clickType]
    }

    document.getElementById('element-result').innerText = JSON.stringify(elementResult);
    event.preventDefault();
}

(function () {
    // get mouse position
    document.addEventListener('mousemove', event => {
        document.getElementById('mouse-x-pos').innerText = String(event.clientX);
        document.getElementById('mouse-y-pos').innerText = String(event.clientY);
    });

    // mouse icon - TOP
    const mouseTrigger = document.getElementById('mouse-trigger');
    mouseTrigger.addEventListener('mousedown', event => mouseHoldAndReleaseEvent(event, '', 'mouse-status'));
    mouseTrigger.addEventListener('contextmenu', event => event.preventDefault());
    mouseTrigger.addEventListener('mouseover', event => mouseOverEvent('mouse-over'));

    // mouse icon - BOTTOM
    const mouseTrigger2 = document.getElementById('mouse-trigger2');
    mouseTrigger2.addEventListener('mousedown', event => mouseHoldAndReleaseEvent(event, '2', 'mouse-status'));
    mouseTrigger2.addEventListener('contextmenu', event => event.preventDefault());
    mouseTrigger2.addEventListener('mouseover', event => mouseOverEvent('mouse-over2'));

    // git icon
    const mouseTrigger3 = document.getElementById('mouse-trigger3');
    mouseTrigger3.addEventListener('mousedown', event => mouseHoldAndReleaseEvent(event, '-Hold', 'mouse-status2'));
    mouseTrigger3.addEventListener('mouseup', event => mouseHoldAndReleaseEvent(event, '-Release', 'mouse-status2'));
    mouseTrigger3.addEventListener('contextmenu', event => event.preventDefault())
})();