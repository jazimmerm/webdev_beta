import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import interactionPlugin from '@fullcalendar/interaction';
import 'rrule';


document.addEventListener('DOMContentLoaded', function() {
    let calendarEl = document.getElementById('calendar');
    let calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: [ 'dayGridPlugin', 'timeGridPlugin', 'interactionPlugin', 'rrulePlugin' ],
        defaultView: 'timeGridWeek',
        editable: true,
        droppable: true,
        height: 'parent',
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay'
            },
        nowIndicator: true,
        selectable: true,
        dateClick: function(info){
            var view = calendar.view;
            if (view.type == 'dayGridMonth'){
                calendar.changeView('timeGridWeek');
                }
            if (view.type == 'timeGridWeek'){
                calendar.changeView('timeGridDay');
            }
            calendar.gotoDate(info.dateStr);
            calendar.select(info.dateStr);
            },
        /* -- This should totally work but it doesn't and I don't know why --
        dayRender: function(dayRenderInfo) {
        var element = dayRenderInfo.el;
        var view = dayRenderInfo.view;
        var date = dayRenderInfo.date;
        element.ondblclick = function(view, date) {
        if (view.type == 'dayGridMonth'){
            calendar.changeView('timeGridWeek');
            }
        if (view.type == 'timeGridWeek'){
            calendar.changeView('timeGridDay');
        }
        calendar.gotoDate(date.dateStr);
        calendar.select(date.dateStr);
        };
        },
        */
        events: [
            {% for appt in appointments %}
                {
                title: "{{appt.patient_name}}",
                start: "{{appt.time_start|date:"Y-m-d H:i"}}",
                end: "{{appt.time_end|date:"Y-m-d H:i"}}"
                },
            {% endfor %}
            ],
        });
    calendar.render();
});