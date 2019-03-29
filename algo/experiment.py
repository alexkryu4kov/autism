import pandas as pd

from random import choice


class Experiment:
    def __init__(self, data='../data.csv'):
        self.data = pd.read_csv(data)
        self.first = self.data[self.data['level'] == 1].reset_index(inplace=True)
        self.second = self.data[self.data['level'] == 2].reset_index(inplace=True)
        self.third = self.data[self.data['level'] == 3].reset_index(inplace=True)

    def get_data(self):
        return self.data

    def choose_elem(self, level):
        links_list = []
        words_list = []
        dataset = self.data[self.data['level'] == level].reset_index()
        for i in range(3):

            rand = choice(list(range(5)))
            links_list.append(dataset.iloc[rand]['picture'])
            words_list.append(dataset.iloc[rand]['word'])
        return links_list, words_list
