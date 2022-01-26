"use strict";

var elementResult = { data: [] };
var keysPressed = [];

(function() {
    selectText('botcity');
    handleMouseEvents();
    handleKeyEvents();
})();

function selectText(elementId) {
    var element = document.getElementById(elementId);
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

function handleMouseEvents() {
    // get mouse position
    document.addEventListener('mousemove', event => {
        document.getElementById('mouse-x-pos').innerText = event.clientX;
        document.getElementById('mouse-y-pos').innerText = event.clientY;
    });

    // select the element on which to handle mouse events
    var element = document.getElementById('mouse-trigger');

    element.addEventListener('mouseover', event => {
        elementResult.data = ['mouse-over'];
        setEventStatus(JSON.stringify(elementResult))
    });

    // get mouse events
    element.addEventListener('mousedown', event => {
        var mouseStatus = document.getElementById('mouse-status');

        if (elementResult.data[0] == 'mouse-over') {
            elementResult.data.shift();
        }

        var clickType = '';
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
        mouseStatus.innerText = clickType;

        elementResult.data.push(clickType)

        setEventStatus(JSON.stringify(elementResult));

        event.preventDefault();
    });

    element.addEventListener('contextmenu', event => {
        event.preventDefault();
    });

    // select the element on which to handle mouse events
    var element2 = document.getElementById('mouse-trigger2');

    element2.addEventListener('mouseover', event => {
        elementResult.data = ['mouse-over2'];
        setEventStatus(JSON.stringify(elementResult))
    });

    // get mouse events
    element2.addEventListener('mousedown', event => {
        var mouseStatus = document.getElementById('mouse-status');

        if (elementResult.data[0] == 'mouse-over2') {
            elementResult.data.shift();
        }

        var clickType = '';
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
        mouseStatus.innerText = clickType;

        elementResult.data.push(clickType)

        setEventStatus(JSON.stringify(elementResult));

        event.preventDefault();
    });

    element2.addEventListener('contextmenu', event => {
        event.preventDefault();
    });
}

function handleKeyEvents() {
    document.onkeydown = event => { return false; }; // disable keydown events
    document.onkeyup = event => { return false; }; // disable keyup events

    var keyboardStatus = document.getElementById('keyboard-status');

    document.addEventListener('keydown', event => {

        // control+r shortcut to reset all values
        if (keysPressed[keysPressed.length - 1] == 'Control' && event.key == 'r') {
            reset();
            return;
        }

        if (event.key != keysPressed[keysPressed.length - 1]) {
            if (event.key == ' ') {
                keysPressed.push('Space');
            } else {
                keysPressed.push(event.key);
            }
        } else {
            return;
        }

        // set keys pressed on keyboard status
        keyboardStatus.innerText = keysPressed.join(' ')

        elementResult.data = keysPressed;

        setEventStatus(JSON.stringify(elementResult))

        event.preventDefault();
    });
}

function reset() {
    keysPressed = [];

    var keyboardStatus = document.getElementById('keyboard-status');
    keyboardStatus.innerText = 'Non key pressed';

    var mouseStatus = document.getElementById('mouse-status');
    mouseStatus.innerText = 'Non clicked';

    elementResult.data = [];

    setEventStatus('')
}

function setEventStatus(value) {
    document.getElementById('element-result').innerText = value;
}

function imageClick(element) {
    elementResult.data = [element];
    setEventStatus(JSON.stringify(elementResult))
}