voting_data = list(open("voting_record_dump109.txt"))
democrats = set()
republicans = set()
votes = dict()

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example:
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data.
    """
    voting_dict = dict()
    for senator in voting_data:
        record = senator.strip().split(" ")
        voting_dict[record[0]] = [int(x) for x in record[3:]]
        if record[1] == 'D':
            democrats.add(record[0])
        else:
            republicans.add(record[0])
    return voting_dict

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    if sen_a in voting_dict and sen_b in voting_dict:
        return sum([voting_dict[sen_a][i]*voting_dict[sen_b][i] for i in list(range(len(voting_dict[sen_b])))])
    else:
        return 0.0


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    similar_senator = ""
    similar_score = 0

    senator_gen = (senator for senator in voting_dict.keys() if senator != sen)
    for senator in senator_gen:
        senator_score = policy_compare(senator, sen, voting_dict)
        if senator_score > similar_score:
            similar_score = senator_score
            similar_senator = senator

    return similar_senator


## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    disimilar_senator = ""
    disimilar_score = 100000

    senator_gen = (senator for senator in voting_dict.keys() if senator != sen)
    for senator in senator_gen:
        senator_score = policy_compare(senator, sen, voting_dict)
        if senator_score < disimilar_score:
            disimilar_score = senator_score
            disimilar_senator = senator

    return disimilar_senator



## Task 5

most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold'



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    similarities = list()
    senator_gen = (senator for senator in sen_set if senator != sen)
    for senator in senator_gen:
        similarities.append(policy_compare(sen, senator, voting_dict))
    return sum(similarities)/len(similarities)

def find_most_similar(sen_set, voting_dict):
    similar_senator = ""
    similar_score = 0
    for senator in sen_set:
        senator_score = find_average_similarity(senator, sen_set, voting_dict)
        print(senator+' '+str(senator_score))
        if senator_score > similar_score:
            similar_score = senator_score
            similar_senator = senator

    return similar_senator


most_average_Democrat = "Biden" # give the last name (or code that computes the last name)


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example:
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    senator_sum = list()
    for senator in sen_set:
        if len(senator_sum) == 0:
            senator_sum = voting_dict[senator]
        else:
            senator_sum = [x+y for (x,y) in zip(senator_sum, voting_dict[senator])]
    return [x/len(sen_set) for x in senator_sum]

def find_most_average_record(sen_set, voting_dict):
    average_record = find_average_record(sen_set, votes)
    similar_senator = ""
    similar_score = 0
    for senator in sen_set:
        senator_score = sum([voting_dict[senator][i]*average_record[i] for i in list(range(len(average_record)))])
        if senator_score > similar_score:
            similar_score = senator_score
            similar_senator = senator

    return similar_senator

def find_least_average_record(sen_set, voting_dict):
    average_record = find_average_record(sen_set, voting_dict)
    disimilar_senator = ""
    disimilar_score = 1000000
    for senator in sen_set:
        senator_score = sum([voting_dict[senator][i]*average_record[i] for i in list(range(len(average_record)))])
        if senator_score < disimilar_score:
            disimilar_score = senator_score
            disimilar_senator = senator

    return disimilar_senator

average_Democrat_record = [-0.16279069767441862, -0.23255813953488372, 1.0, 0.8372093023255814, 0.9767441860465116, -0.13953488372093023, -0.9534883720930233, 0.813953488372093, 0.9767441860465116, 0.9767441860465116, 0.9069767441860465, 0.7674418604651163, 0.6744186046511628, 0.9767441860465116, -0.5116279069767442, 0.9302325581395349, 0.9534883720930233, 0.9767441860465116, -0.3953488372093023, 0.9767441860465116, 1.0, 1.0, 1.0, 0.9534883720930233, -0.4883720930232558, 1.0, -0.32558139534883723, -0.06976744186046512, 0.9767441860465116, 0.8604651162790697, 0.9767441860465116, 0.9767441860465116, 1.0, 1.0, 0.9767441860465116, -0.3488372093023256, 0.9767441860465116, -0.4883720930232558, 0.23255813953488372, 0.8837209302325582, 0.4418604651162791, 0.9069767441860465, -0.9069767441860465, 1.0, 0.9069767441860465, -0.3023255813953488] # (give the vector)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example:
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    least_average_sentor = find_least_average_record(voting_dict.keys(), voting_dict)
    least_similar_toLeast_average_senator = least_similar(least_average_sentor, voting_dict)
    return (least_average_sentor, least_similar_toLeast_average_senator)

votes = create_voting_dict()