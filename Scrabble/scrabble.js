Scrabble.set = new Map();
Scrabble.set("a",1);
Scrabble.set("b",3);
Scrabble.set("c",3);
Scrabble.set("d",2);
Scrabble.set("e",1);
Scrabble.set("f",4);
Scrabble.set("g",2);

const mot = "bonjour";
let score = 0;

for (let i = 0; i < mot.length; i++) {
    score += Scrabble.set(mot[i]);
}

console.log(score);
