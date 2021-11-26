from os import EX_CANTCREAT


def Extract():
    cnt = 0
    f2 = open('entity2id.txt','w')
    with open('entity_with_text.txt') as f:
        entity_list = f.readlines()
        f2.write(str(len(entity_list)))
        f2.write('\n')
        for entity in entity_list:
            entity = entity.split('\t')
            f2.write(entity[0])
            f2.write('\t')
            f2.write(str(cnt))
            f2.write('\n')
            cnt += 1


if __name__ == '__main__':
    Extract()
