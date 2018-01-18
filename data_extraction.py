def splitTrainTest(self, df, test_ratio, seed=1):
    """
    Split Dataframe into train and test set randomly.

    Parameters
    ----------
    df
        type : pandas.DataFrame
        desc : target dataset to split
    test_ratio
        type : float
        desc : ratio of the test set (value must be between 0 and 1)
    seed
        type : int
        desc : seed generator

    Returns
    -------
    type : pandas.DataFrame
    desc : test set

    """
    np.random.seed(seed)
    shuffled_indices = np.random.permutation(len(df))
    test_set_size = int(len(df) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]

    train_set = pd.DataFrame()
    test_set = pd.DataFrame()
    train_set = train_set.append(df.iloc[train_indices])
    test_set = test_set.append(df.iloc[test_indices])
    return train_set, test_set


def splitTrainTestStratified(self, df, test_ratio, seed, target_column):
    """
    Split Dataframe into train and test set with stratified method.

    Parameters
    ----------
    df
        type : pandas.DataFrame
        desc : target dataset to split
    target_column
        type : string
        desc : key of the column to stratified
    test_ratio
        type : float
        desc : ratio of the test set (value must be between 0 and 1)
    seed
        type : int
        desc : seed generator

    Returns
    -------
    type : pandas.DataFrame
    desc : test set

    """
    split = StratifiedShuffleSplit(
            n_splits=1,
            test_size=test_ratio,
            random_state=seed)

    for train_index, test_index in split.split(df, df[target_column]):
        strat_train_set = df.loc[train_index]
        strat_test_set = df.loc[test_index]

    train_set = pd.DataFrame()
    test_set = pd.DataFrame()
    train_set = train_set.append(strat_train_set)
    test_set = test_set.append(strat_test_set)
    return train_set, test_set