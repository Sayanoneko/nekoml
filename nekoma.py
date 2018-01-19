from data_extraction import splitTrainTest, splitTrainTestStratified
import pandas as pd
import pandas_profiling as pdp
from IPython.display import display
import io
import preprocess_vis as prv


class Nekoma:

    def __init__(self, method=None, **kwargs):
        if method is None:
            self.train_set = pd.DataFrame()
            self.test_set = pd.DataFrame()
            self.target = pd.DataFrame()
            self.back_up = self.train_set.copy()
            self.transformations = list()
            self.counter = 0

        elif method == "df":
            df = kwargs.get("df")
            target = kwargs.get("target")
            test_ratio = kwargs.get("test_ratio", 0.2)
            seed = kwargs.get("seed", 1)
            strat = kwargs.get("strat", False)
            if strat is False:
                self.train_set, self.test_set = splitTrainTest(
                    df, test_ratio, seed)
            else:
                self.train_set, self.test_set = splitTrainTestStratified(
                    df, target, test_ratio, seed)
            self.target = target
            self.back_up = self.train_set.copy()
            self.transformations = []

        elif method == "file":
            file_path = kwargs.get("file_path")
            target = kwargs.get("target")
            test_ratio = kwargs.get("test_ratio", 0.2)
            seed = kwargs.get("seed", 1)
            strat = kwargs.get("strat", None)
            if type(df_or_file) == "str":
                extension = file.split(".")[1]
                if extension == "csv":
                    df = pd.read_csv(file_path, **kwargs.get(dict_param))
                elif extension == "json":
                    df = pd.read_json(file_path)
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
            self.transformations = []

    def reset(self):
        self.train_set = pd.DataFrame()
        self.train_set = self.back_up.copy()
        tr_counter = 0
        self.transformations = []

    def setTrainSet(self, train_set):
        self.train_set = train_set
        self.back_up = self.train_set.copy()

    def setTestSet(self, test_set):
        self.test_set = test_set

    def setTarget(self, target):
        self.target = target

    def info(self):
        prv.info(self.train_set)

    def desc(self):
        prv.desc(self.train_set)

    def report(self):
        prv.report(self.train_set)

    def apply(self, transformation_f, parameters):
        tr_counter += 1
        self.transformations.append((str(get_counter()) +
                                    ". " + type(transformation).__name__,
                                    transformation))
        transformation_f(self.train_set, **parameters)

    def use_pipeline(self, df, name, update=True):
        """
        Use a pipeline by giving the associated name on a dataframe.

        Parameters
        ----------
            df
                type : Dataframe
            name
                type : string

        """
        for pipeline in self.tr_transformation_pipelines_collection:
            if pipeline[0] == name:
                pipeline[1].fit_transform(df)
                if update:
                    for transformation in pipeline[1].steps:
                        self.add_transformation(transformation[1])
                break


