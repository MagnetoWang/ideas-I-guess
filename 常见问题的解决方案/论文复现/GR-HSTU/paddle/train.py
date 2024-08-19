
class HSTU(GeneralizedInteractionModule):
    """
    Implements HSTU (Hierarchical Sequential Transduction Unit) in 
    Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations,
    https://arxiv.org/abs/2402.17152.

    Note that this implementation is intended for reproducing experiments in
    the traditional sequential recommender setting (Section 4.1.1), and does
    not yet use optimized kernels discussed in the paper.
    """

@gin.configurable
def train_fn(
    # 优化器参数
    learning_rate: float = 1e-3,
    # 一阶矩估计的指数衰减率
    beta1: float = 0.9,
    beta2: float = 0.98,
    weight_decay: float = 1e-3,
    # epoch训练参数
    num_epochs: int = 100,

):
    # set cpu gpu config


    # build data loader and data sample
    train_data_sampler, train_data_loader = create_data_loader(
        dataset.train_dataset,
        batch_size=local_batch_size,
        world_size=world_size,
        rank=rank,
        shuffle=True,
        drop_last=world_size > 1,
    )



    # model function
    model = paddle.nn.linear(10, 10)
    # loss funciton

    # opt function
    opt = paddle.optimizer.Adamw(parameters=model.parameters(), learning_rate=learning_rate, beta1=beta1, beta2=beta2, weight_decay=weight_decay)

    batch_id = 0
    for epoch in range(num_epochs):
        model.train()
        for row in iter(train_data_loader):
            # extract feature
            seq_features, target_ids, target_ratings = movielens_seq_features_from_row(
                row, device=device, max_output_length=gr_output_length + 1,
            )

           

            input_embeddings = model.module.get_item_embeddings(seq_features.past_ids)
            seq_embeddings = model(
                past_lengths=seq_features.past_lengths,
                past_ids=seq_features.past_ids,
                past_embeddings=input_embeddings,
                past_payloads=seq_features.past_payloads,
            )  # [B, X]

            # 负采样


            # loss
            loss = ar_loss(
                lengths=seq_features.past_lengths,  # [B],
                output_embeddings=seq_embeddings[:, :-1, :],  # [B, N-1, D]
                supervision_ids=supervision_ids[:, 1:],  # [B, N-1]
                supervision_embeddings=input_embeddings[:, 1:, :],  # [B, N - 1, D]
                supervision_weights=ar_mask.float(),
                negatives_sampler=negatives_sampler,
            )  # [B, N]

            loss.backward()


            opt.step() 
            # 清零
            opt.clear_grad()

            batch_id += 1











    # epoch


    # predict



    # save model

def main(argv):
    train()
    # world_size = torch.cuda.device_count()

    # mp.set_start_method('forkserver')
    # mp.spawn(mp_train_fn,
    #          args=(world_size, FLAGS.master_port, FLAGS.gin_config_file),
    #          nprocs=world_size,
    #          join=True)


if __name__ == "__main__":
    app.run(main)