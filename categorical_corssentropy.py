import math

def crossentropy_multiple(pred_v_group, true_v_group):

    sum = 0

    for pred_v_list, true_v_list in zip(pred_v_group, true_v_group):
        for p_v, t_v in zip(pred_v_list, true_v_list):
            sum += math.log(p_v) * t_v

    sum = -sum
    return sum/len(pred_v_group)

def crossentropy_binary(pred_v_group, true_v_group):

    sum = 0

    for pred_v_list, true_v_list in zip(pred_v_group, true_v_group):
        for pred_v, true_v in zip(pred_v_list, true_v_list):
            sum += math.log(pred_v) * true_v + math.log(1 - pred_v) * (1 - true_v)
    sum = -sum
    return sum/len(pred_v_group)

if __name__ == '__main__':
    print(crossentropy_multiple([[.1, .2, .7], [.1, .7, .2], [.3, .4, .3]], [[0, 0, 1], [0, 1, 0], [1, 0, 0]]))
    print(crossentropy_binary([[.3, .7], [.1, .9], [.3, .7]], [[0, 1], [0, 1], [1, 0]]))