import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return {i + 1: finishers[place] for i, place in enumerate(sorted(finishers.keys()))}


class TournamentTest(unittest.TestCase):
    # all_results = {}
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.name1 = Runner('Усэйн', 10)
        self.name2 = Runner('Андрей', 9)
        self.name3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results:
            # print(cls.all_results)
            print(key)
            for i in cls.all_results[key]:
                # print(i)
                print(f'{cls.all_results[key][i]} - {i}')
            print()


    def test_run_1(self):
        test_tournament = Tournament(90, self.name1, self.name3)
        a = test_tournament.start()
        # print(res)
        self.all_results['Усейн и Ник'] = a
        key = max(a.keys())
        self.assertTrue(a[key] == self.name3)

    def test_run_2(self):
        test_tournament = Tournament(90,self.name2, self.name3)
        a = test_tournament.start()
        self.all_results['Андрей и Ник'] = a
        key = max(a.keys())
        self.assertTrue(a[key] == self.name3)

    def test_run_3(self):
        test_tournament = Tournament(90, self.name1, self.name2, self.name3)
        a = test_tournament.start()
        self.all_results['Усейн, Андрей и Ник'] = a
        key = max(a.keys())
        self.assertTrue(a[key] == self.name3)


if __name__ == '__main__':
    unittest.main()