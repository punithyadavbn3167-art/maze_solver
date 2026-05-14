const rows = 20
const cols = 20

let grid = []
let startPos = null
let goalPos = null
let mode = "wall"

const gridElement = document.getElementById("grid")


function setMode(m){
    mode = m
}


function createGrid(){

    gridElement.innerHTML = ""

    for(let r=0; r<rows; r++){

        grid[r] = []

        for(let c=0; c<cols; c++){

            const cell = document.createElement("div")
            cell.classList.add("cell")

            cell.addEventListener("click", () => handleClick(r,c,cell))

            gridElement.appendChild(cell)

            grid[r][c] = 0
        }
    }
}


function handleClick(r,c,cell){

    if(mode === "wall"){

        cell.classList.toggle("wall")

        grid[r][c] = cell.classList.contains("wall") ? 1 : 0
    }

    if(mode === "start"){

        removeClass("start")

        cell.classList.add("start")

        startPos = [r,c]
    }

    if(mode === "goal"){

        removeClass("goal")

        cell.classList.add("goal")

        goalPos = [r,c]
    }
}

function removeClass(name){

    const elements = document.getElementsByClassName(name)

    while(elements.length > 0){

        elements[0].classList.remove(name)
    }
}


async function solveMaze(){

    if(!startPos || !goalPos){

        alert("Please set start and goal")

        return
    }

    const algorithm = document.getElementById("algorithm").value

    const response = await fetch("http://127.0.0.1:8000/solve-maze", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            maze: grid,
            start: startPos,
            goal: goalPos,
            algorithm: algorithm
        })
    })

    const data = await response.json()

    animatePath(data.path)
}


function animatePath(path){

    path.forEach((pos,i)=>{

        setTimeout(()=>{

            const index = pos[0] * cols + pos[1]

            const cell = document.getElementsByClassName("cell")[index]

            if(!cell.classList.contains("start") &&
               !cell.classList.contains("goal")){

                cell.classList.add("path")
            }

        }, i * 100)

    })
}


function clearGrid(){

    startPos = null
    goalPos = null

    createGrid()
}


createGrid()