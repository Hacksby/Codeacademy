let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;

// Write your code below:
const generateTarget = () => Math.floor(Math.random() * 10)

const getAbsoluteDistance = (guess, secret) => secret - guess

const compareGuesses = (gHum, gCom, gSec) =>
{
  distHum = getAbsoluteDistance(gHum, gSec)
  distCom = getAbsoluteDistance(gCom, gSec)

  if (distHum < 0)
    distHum *= -1
  if (distCom < 0)
    distCom *= -1

  if ((gHum === gCom) || (distHum <= distCom))
    return true
  else
    return false
}

const updateScore = winner =>
{
  if (winner === 'human')
    humanScore += 1
  if (winner === 'computer')
    computerScore += 1
}

const advanceRound = () => currentRoundNumber+=1
