class Clock:
    time = 0
    timers = []

    def set_timer(self, t):
        cur_timer = self.format(t)
        self.timers.append(cur_timer)
        self.timers.append(cur_timer + 24 * 60)
        self.timers.sort()
        h, m = t.split(':')
        h, m = '0' * (2 - len(h)) + h, '0' * (2 - len(m)) + m
        print('Alarm clock set on', h + ':' + m)

    def time_rest(self):
        if len(self.timers) == 0:
            print('No set alarm clocks')
            return
        next = None
        for e in self.timers:
            if e >= self.time:
                next = e
                break
        print('The nearest alarm clock will go off after', self.back_format(next - self.time) + '.')

    def change_time(self, t):
        h, m = t.split(':')
        h, m = '0' * (2 - len(h)) + h, '0' * (2 - len(m)) + m
        print('Time set at', h + ':' + m)
        self.time = self.format(t)
        prev = None
        for e in self.timers:
            if e <= self.time:
                prev = e
            else:
                break
        if prev != None:
            if prev == self.time:
                print('Start of the alarm!')
                while self.time in self.timers:
                    self.timers.remove(self.time)
                while self.time + 24 * 60 in self.timers:
                    self.timers.remove(self.time + 24 * 60)
            else:
                h, m = str(prev // 60), str(prev % 60)
                h, m = '0' * (2 - len(h)) + h, '0' * (2 - len(m)) + m
                print('You missed the alarm clock ' + h + ':' + m + '!')

    def format(self, t):
        h, m = map(int, t.split(':'))
        return h * 60 + m

    def back_format(self, t):
        h, m = t // 60, t % 60
        if h:
            return self.hours(h) + ' and ' + self.minuts(m)
        else:
            return self.minuts(m)

    def hours(self, h):
        if h == 1:
            return '1 hour'
        elif h < 5:
            return str(h) + ' hour'
        else:
            return str(h) + ' hour'

    def minuts(self, m):  # 0,5-20,25-30,35-40 минут 1,21,31 минута 2-4,22-24,32-34 минуты
        if 5 <= m and m <= 20:
            return str(m) + ' minute'
        else:
            if m % 10 == 1:
                return str(m) + ' minute'
            elif m % 10 == 0 or m % 10 < 5:
                return str(m) + ' minutes'
            else:
                return str(m) + ' minute'


clock = Clock()
request = input()
while request != '0':
    if request[0] == '1':
        clock.set_timer(request[2:])
    elif request == '2':
        clock.time_rest()
    else:
        clock.change_time(request[2:])
    request = input()
