(function () {
    document.onkeydown = event => {
        return false;
    }; // disable keydown events

    document.onkeyup = event => {
        return false;
    }; // disable keyup events

    document.addEventListener('keydown', event => {

        // CONTROL+r -> Shortcut to Reset all Values
        if (keysPressed[keysPressed.length - 1] === 'Control' && event.key === 'r') {
            document.getElementById('keyboard-status').innerText = 'Non key pressed';
            document.getElementById('mouse-status').innerText = 'Non clicked';
            document.getElementById('mouse-status2').innerText = 'Non clicked';
            document.getElementById('element-result').innerText = '';

            keysPressed = [];
            elementResult.data = [];
            return;
        }

        // SHIFT+P trigger -> Show Alert
        if (keysPressed[keysPressed.length - 1] === 'Shift' && event.key === 'P') {
            alert("Alert test");
            return;
        }

        // SHIFT+D trigger -> Scroll Automatically to the Bottom of the Page
        if (keysPressed[keysPressed.length - 1] === 'Shift' && event.key === 'D') {
            window.scrollTo(0, 1000)
        }

        // SHIFT+L trigger -> Show Prompt
        if (keysPressed[keysPressed.length - 1] === 'Shift' && event.key === 'L') {
            elementResult.data = [prompt('Message test')];
            document.getElementById('element-result').innerText = JSON.stringify(elementResult);
            return;
        }

        // SHIFT+Q -> Download file
        if (keysPressed[keysPressed.length - 1] === 'Shift' && event.key === 'Q') {
            window.location.href = 'fake.bin'; // local file
            // window.location.href = 'https://speed.hetzner.de/100MB.bin';
        }


        if (event.key !== keysPressed[keysPressed.length - 1]) {
            if (event.key === ' ') { // when space key is pressed
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
