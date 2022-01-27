function imageClick(element) {
    let elementResult = {data: []};
    elementResult.data = [element];
    document.getElementById('element-result').innerText = JSON.stringify(elementResult);
}
