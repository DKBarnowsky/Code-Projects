const daysEL = document. getElementById('days')
const hoursEL = document. getElementById('hours')
const minEL = document. getElementById('mins')
const secondsEL = document. getElementById('seconds')



const newYears = '1 Jan 2024'

function countdown() {
    const newYearsDate = new Date(newYears);
    const currentDate = new Date();

    const totalSeconds = (newYearsDate - currentDate) / 1000;

    const days = Math.floor(totalSeconds /3600 /24);
    const hours = Math.floor(totalSeconds / 3600) % 24;
    const mins = Math.floor(totalSeconds / 60) % 60;
    const seconds = Math.floor(totalSeconds) % 60;

    daysEL.innerHTML = days; 
    hoursEL.innerHTML = formatTime(hours); 
    minEL.innerHTML = formatTime(mins); 
    secondsEL.innerHTML = formatTime(seconds); 
}

function formatTime(time) {
    return time < 1 ? ('0') : time;
}

//initial call
countdown();

setInterval(countdown, 1000)

