const Scrabble = {
    set: new Map([
        ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
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

    motsAvecScores.sort((a, b) => b.score - a.score);

    const resultat = motsAvecScores.map(item => `${item.mot} (${item.score})`).join('<br>');
    document.getElementById('score').innerHTML = "Résultat des mots :" + resultat;
    console.table(motsAvecScores);
}
