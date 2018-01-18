from data_extraction import splitTrainTest, splitTrainTestStratified
import pandas as pd
import pandas_profiling as pdp    return    return pdp.ProfileReport(df)
        except:
            print("Error: can't show report") pdp.ProfileReport(df)
        except:
            print("Error: can't show report")
from IPython.display import display



class Nekoma:

    def __init__(self):
        self.train_set = pd.Dataframe()
        self.test_set = pd.Dataframe()
        self.target = pd.Dataframe()
        self.back_up = self.train_set.copy()

    def __init__(train_set, test_set, target):
        self.train_set = train_set
        self.test_set = test_set
        self.target = target
        self.back_up = self.train_set.copy()

    def __init__(df_or_file, target, test_ratio, seed=1, strat=False):
        if type(df_or_file) == "str":
            extension = file.split(".")[1]
            if extension == "csv":
                df = pd.read_csv(file, **dict_param)
            elif extension == "json":
                df = pd.read_json(file)
            if strat:
                self.train_set, self.test_set = splitTrainTest(
                    df, target, test_ratio, seed)
            else:
                self.train_set, self.test_set = splitTrainTestStratified(
                    df, target, test_ratio, seed)
        else:
            if strat:
                self.train_set, self.test_set = splitTrainTest(
                    df_or_file, target, test_ratio, seed)
            else:
                self.train_set, self.test_set = splitTrainTestStratified(
                    df_or_file, target, test_ratio, seed)
        self.target = target
        self.back_up = self.train_set.copy()

    def reset(self):
        self.train_set = pd.Dataframe()
        self.train_set = self.back_up.copy()

    def setTrainSet(self, train_set):
        self.train_set = train_set
        self.back_up = self.train_set.copy()

    def setTestSet(self, test_set):
        self.test_set = test_set

    def setTarget(self, target):
        self.target = target

    def info(self):
        dict_df = {"Feature":[], "Non NA":[], "Type":[]}
        for line in self.train_set.split("\n")[3:-3]:
            dict_df["Feature"].append(line.split("    ")[0])
            dict_df["Non NA"].append(line.split("    ")[1].split(" ")[0])
            dict_df["Type"].append(line.split("    ")[1].split(" ")[2])
        df = pd.DataFrame(dict_df)

    def desc(self):
        try:
            display(df.select_dtypes(include=['object']).describe())
            print("")
        except:
            print("There are no object columns")
            print("")
        try:
            display(df.select_dtypes(include=[np.float]).describe())
            print("")
        except:
            print("There are no float columns")
            print("")
        try:
            display(df.select_dtypes(include=[np.int]).describe())
        except:
            print("There are no int columns")
        return None

    def report(self):
        try:
            return pdp.ProfileReport(df)
        except:
            print("Error: can't show report")

