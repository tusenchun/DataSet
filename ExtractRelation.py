from os import EX_CANTCREAT


def Extract():
    cnt = 0
    f2 = open('relation2id.txt','w')
    with open('relation_with_text.txt') as f:
        relation_list = f.readlines()
        f2.write(str(len(relation_list)))
        f2.write('\n')
        for relation in relation_list:
            relation = relation.split('\t')
            f2.write(relation[0])
            f2.write('\t')
            f2.write(str(cnt))
            f2.write('\n')
            cnt += 1


if __name__ == '__main__':
    Extract()
