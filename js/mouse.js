function mouseHoldAndReleaseEvent(event, mouseEvent, mouseStatusId) {
    let clickType = '';
    switch (event.button) {
        case 0:
            clickType = `Left${mouseEvent}`;
            break;
        case 1:
            clickType = `Middle${mouseEvent}`;
            break;
        case 2:
            clickType = `Right${mouseEvent}`;
            break;
    }

    document.getElementById(mouseStatusId).innerText = clickType;

    elementResult.data = [clickType]
    document.getElementById('element-result').innerText = JSON.stringify(elementResult);
    event.preventDefault();
}

(function () {
    // get mouse position
    document.addEventListener('mousemove', event => {
        document.getElementById('mouse-x-pos').innerText = String(event.clientX);
        document.getElementById('mouse-y-pos').innerText = String(event.clientY);
    });

    const body = document.getElementById('mouse-trigger3');
    body.addEventListener('mousedown', event =>
        mouseHoldAndReleaseEvent(event, '-Hold', 'mouse-status2'));

    body.addEventListener('mouseup', event =>
        mouseHoldAndReleaseEvent(event, '-Release', 'mouse-status2'));

    body.addEventListener('contextmenu', event => event.preventDefault())

    // select the element on which to handle mouse events
    const mouseTop = document.getElementById('mouse-trigger');
    mouseTop.addEventListener('mouseover', event => {
        elementResult.data = ['mouse-over'];
        document.getElementById('element-result').innerText = JSON.stringify(elementResult);
    });

    // get mouse events
    mouseTop.addEventListener('mousedown', event => {
        if (elementResult.data[0] === 'mouse-over') {
            elementResult.data.shift();
        }

        let clickType = '';
        switch (event.button) {
            case 0:
                clickType = 'Left';
                break;
            case 1:
                clickType = 'Middle';
                break;
            case 2:
                clickType = 'Right';
                break;
        }

        // set click type on mouse status
        document.getElementById('mouse-status').innerText = clickType;

        elementResult.data.push(clickType)
        document.getElementById('element-result').innerText = JSON.stringify(elementResult);
    });

    mouseTop.addEventListener('contextmenu', event => {
        event.preventDefault();
    });


    // select the element on which to handle mouse events
    const mouseBottom = document.getElementById('mouse-trigger2');
    mouseBottom.addEventListener('mouseover', event => {
        elementResult.data = ['mouse-over2'];
        document.getElementById('element-result').innerText = JSON.stringify(elementResult);
    });

    // get mouse events
    mouseBottom.addEventListener('mousedown', event => {
        if (elementResult.data[0] === 'mouse-over2') {
            elementResult.data.shift();
        }

        let clickType = '';
        switch (event.button) {
            case 0:
                clickType = 'Left2';
                break;
            case 1:
                clickType = 'Middle2';
                break;
            case 2:
                clickType = 'Right2';
                break;
        }

        // set click type on mouse status
        document.getElementById('mouse-status').innerText = clickType;

        elementResult.data.push(clickType)
        document.getElementById('element-result').innerText = JSON.stringify(elementResult);

        event.preventDefault();
    });

    mouseBottom.addEventListener('contextmenu', event => event.preventDefault());
})();