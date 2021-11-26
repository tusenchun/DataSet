from os import EX_CANTCREAT

def Extract():
    # train
    with open('train.txt') as f:
        f2 = open('train2id.txt','w')
        train_list = f.readlines()
        f2.write(str(len(train_list)))
        f2.write('\n')
        for train in train_list:
            train = train.split('\t')
            f2.write(train[0])
            f2.write(' ')
            f2.write(train[1])
            f2.write(' ')
            f2.write(train[2])

   
    # valied
    with open('dev.txt') as f:
        f2 = open('valid2id.txt','w')
        valid_list = f.readlines()
        f2.write(str(len(valid_list)))
        f2.write('\n')
        for valid in valid_list:
            valid = valid.split('\t')
            f2.write(valid[0])
            f2.write(' ')
            f2.write(valid[1])
            f2.write(' ')
            f2.write(valid[2])

               
    # test
    with open('test.txt') as f:
        f2 = open('test2id.txt','w')
        test_list = f.readlines()
        f2.write(str(len(test_list)))
        f2.write('\n')
        for test in test_list:
            test = test.split('\t')
            f2.write(test[0])
            f2.write(' ')
            f2.write(test[1])
            f2.write(' ')
            f2.write(test[2])




if __name__ == '__main__':
    Extract()