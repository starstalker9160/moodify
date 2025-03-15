document.addEventListener("DOMContentLoaded", () => {
    const colors = {
        happy: ["#000000", "#EFE2FA", "#BACBFE", "#8F9FE4", "#BCA5D4", "#7164B4"],
        anger: ["#000000", "#F7B538", "#DB7C26", "#D8572A", "#C32F27", "#780116"],
        anxiousness: ["#000000", "#C8D53E", "#A3C844", "#84BE4A", "#609E43", "#3C6C3B"]
    };

    function isLeapYear(year) {
        return (year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0));
    }

    const currentYear = new Date().getFullYear();
    const months = [31, isLeapYear(currentYear) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    async function fetchCSVData() {
        try {
            const response = await fetch('/static/db/moodJournal.csv');
            const csvText = await response.text();

            const parsedData = Papa.parse(csvText, {
                header: true,
                skipEmptyLines: true
            });

            return parsedData.data;
        } catch (error) {
            console.error("Error fetching CSV data:", error);
            return [];
        }
    }

    async function createCalendar(calendarId) {
        const calendarBody = document.querySelector(`#${calendarId} table tbody`);
        const moodData = await fetchCSVData();
        for (let day = 1; day <= 31; day++) {
            const row = document.createElement("tr");
            months.forEach((daysInMonth, monthIndex) => {
                const cell = document.createElement("td");
                row.appendChild(cell);
            });
            calendarBody.appendChild(row);
        }
    }

    createCalendar("calendar-a");
    createCalendar("calendar-b");
    createCalendar("calendar-c");
});
