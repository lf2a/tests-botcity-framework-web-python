(function () {
    const elementResult = {data: []};
    let keysPressed = [];

    document.onkeydown = event => {
        return false;
    }; // disable keydown events

    document.onkeyup = event => {
        return false;
    }; // disable keyup events

    document.addEventListener('keydown', event => {

        // CONTROL+r -> shortcut to reset all values
        if (keysPressed[keysPressed.length - 1] === 'Control' && event.key === 'r') {
            document.getElementById('keyboard-status').innerText = 'Non key pressed';
            document.getElementById('mouse-status').innerText = 'Non clicked';
            document.getElementById('element-result').innerText = '';

            keysPressed = [];
            elementResult.data = [];
            return;
        }

        // SHIFT+P trigger
        if (keysPressed[keysPressed.length - 1] === 'Shift' && event.key === 'P') {
            alert("Alert test");
            return;
        }

        // SHIFT+L trigger
        if (keysPressed[keysPressed.length - 1] === 'Shift' && event.key === 'L') {
            elementResult.data = [prompt('Message test')];
            document.getElementById('element-result').innerText = JSON.stringify(elementResult);
            return;
        }

        if (event.key !== keysPressed[keysPressed.length - 1]) {
            if (event.key === ' ') {
                keysPressed.push('Space');
            } else {
                keysPressed.push(event.key);
            }
        } else {
            // ignore repeated characters
            return;
        }

        // set keys pressed on keyboard status
        document.getElementById('keyboard-status').innerText = keysPressed.join(' ');

        elementResult.data = keysPressed;
        document.getElementById('element-result').innerText = JSON.stringify(elementResult);

        event.preventDefault();
    });
})();
