import re

from course_planner import MoodleQuiz, Seminar, Practica


class Interpreter():

    candidates = {
        MoodleQuiz: re.compile(r'^[q]([0-9]{1,2})([sf]?)$', re.IGNORECASE),
        Seminar: re.compile(r'^[s]([0-9]{1,2})([sf]?)$', re.IGNORECASE),
        Practica: re.compile(r'^[p]([0-9]{1,2})([sf]?)$', re.IGNORECASE),
        }

    def __init__(self, meetings, course):
        self.meetings = meetings
        self.course = course

    def _detect_event_class_and_id(self, string):
        """Returns a tuple of the class and the meeting id."""
        for clazz, regex in self.candidates.items():
            r = regex.search(string)
            if r:
                return (clazz, int(r.groups()[0]))

    def _split_line(self, string):
        parts = string.split(' ')

        if len(parts) != 3:
            raise Exception('Invalid syntax')
        return parts
