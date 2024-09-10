const Scrabble = {
    set: new Map([
        ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
        ['h', 4], ['i', 1], ['j', 8], ['k', 10], ['l', 1], ['m', 2], ['n', 1],
        ['o', 1], ['p', 3], ['q', 8], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
        ['v', 4], ['w', 10], ['x', 10], ['y', 10], ['z', 10]
    ])
};

function Score() {
    const motsInput = document.getElementById('mot').value;
    const mots = motsInput.split(' ').map(mot => mot.trim().toLowerCase());

    if (mots.length !== 5) {
        alert('Veuillez entrer 5 mots séparés par des espaces.');
        return;
    }

    const motsAvecScores = mots.map(mot => {
        let score = 0;
        for (let lettre of mot) {
            score += Scrabble.set.get(lettre) || 0;
        }
        return { mot, score };
    });

    motsAvecScores.sort((a, b) => a.score - b.score);

    const resultat = motsAvecScores.map(item => `${item.mot} (${item.score})`).join(', ');
    document.getElementById('score').textContent = 'résultat des mot : ${resultat}';
}

