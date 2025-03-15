document.addEventListener("DOMContentLoaded", () => {
    function isLeapYear(year) { return (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0)); }
    const currentYear = new Date().getFullYear();
    
    const months = [31, isLeapYear(currentYear) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    function createCalendar(calendarId) {
        const calendarBody = document.querySelector(`#${calendarId} table tbody`);

        for (let day = 1; day <= 31; day++) {
            const row = document.createElement("tr");

            months.forEach((daysInMonth, monthIndex) => {
                const cell = document.createElement("td");

                if (day > daysInMonth) {
                    cell.classList.add("black");
                } else {
                    cell.textContent = "";
                }

                row.appendChild(cell);
            });

            calendarBody.appendChild(row);
        }
    }

    createCalendar("calendar-a");
    createCalendar("calendar-b");
    createCalendar("calendar-c");
});
