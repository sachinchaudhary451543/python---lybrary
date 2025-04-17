def min_max(depth,node_index,maximizing_player,values,alpha,beta):
    if depth ==3:
        return values[node_index]
    
    if maximizing_player:
        max_eval = float('-inf')
        for i in range(2):
            eval = min_max = max(max_eval,eval)
            alpha = max(alpha,eval)
            if beta <= alpha:
                break
            return max_eval
        else:
            min_eval = float('-inf')
            for i in range(2):
                eval = min_max(depth + 1, node_index * 2 + i, True, values,alpha,beta)
                min_eval = min(beta,eval)
                if beta <= alpha:
                    break
                return min_eval
            
    values = [3,12,8,2,6,14,5,4]


    alpha = float('-inf')
    beta = float('-inf')
    optimal_value = min_max(0,0,True,values,alpha,beta)
    print(f"the optimal value for the maximizing player is: {optimal_value}")
    