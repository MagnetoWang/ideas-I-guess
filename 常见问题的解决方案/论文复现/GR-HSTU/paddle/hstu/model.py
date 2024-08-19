"""
Implements HSTU (Hierarchical Sequential Transduction Unit) in 
Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations
(https://arxiv.org/abs/2402.17152).
"""

import paddle
import paddle.nn as nn
import paddle.nn.functional as F

import abc


class LearnablePositionalEmbedding(nn.Layer):
    def __init__(self):

    def forward(self):


class L2NormEmbedding(nn.Layer):
    def __init__(self,
        embedding_dim: int,
        eps: float() = 1e-6
        ) -> None:
        self._embedding_dim = embedding_dim
        self._eps = eps

     def debug_str(self) -> str:
        return "l2"
    
    def forward(self, embeddings: paddle.Tensor) -> paddle.Tensor:
        embeddings = embeddings[..., self._embedding_dim]
        return embeddings / paddle.clip(paddle.linalg.norm(embeddings, p=2, keepdim=True, axis=0), min=self._eps)



class LayerNormEmbedding(nn.Layer):
    def __init__(
        self,
        embedding_dim: int,
        eps: float = 1e-6
    ) -> None:
        self._embedding_dim: int = embedding_dim
        self._eps: float = eps
    
     def debug_str(self) -> str:
        return "layerNorm"

    def forward(
        self,
        embeddings: paddle.Tensor
    ) -> paddle.Tensor:
        embeddings = embeddings[..., self._embedding_dim]
        return F.layer_norm(embeddings
        , normalized_shape)



class GeneralizedRecommender(nn.Layer):
    
    @abc.abstractmethod
    def get_item_embeddings(
        self,
        item_ids: paddle.Tensor,
    ) -> paddle.Tensor:
        pass

    @abc.abstractmethod
    def get_item_sideinfo(
        self,
        item_ids: paddle.Tensor,
    ) -> Optional[paddle.Tensor]:
        pass

    @abc.abstractmethod
    def interaction(
        self,
        input_embeddings: paddle.Tensor,  # [B, D]
        target_ids: paddle.Tensor,  # [1, X] or [B, X]
        target_embeddings: Optional[paddle.Tensor] = None,   # [1, X, D'] or [B, X, D']
    ) -> paddle.Tensor:
        pass

    @abc.abstractmethod
    def debug_str(
        self,
    ) -> str:
        pass

class HSTU(GeneralizedRecommender):
     """
    Implements HSTU (Hierarchical Sequential Transduction Unit) in 
    Actions Speak Louder than Words: Trillion-Parameter Sequential Transducers for Generative Recommendations,
    https://arxiv.org/abs/2402.17152.

    Note that this implementation is intended for reproducing experiments in
    the traditional sequential recommender setting (Section 4.1.1), and does
    not yet use optimized kernels discussed in the paper.
    """

    def __init__(self) -> None:


     def get_item_embeddings(self, ids: paddle.Tensor) ->
     paddle.Tensor:
        pass

    def debug_str(self) -> str:
        debug_str = (
            f"HSTU-b{self._num_blocks}-h{self._num_heads}-dqk{self._dqk}-dv{self._dv}"
            + f"-l{self._linear_activation}d{self._linear_dropout_rate}"
            + f"-ad{self._attn_dropout_rate}"
        )
        if not self._enable_relative_attention_bias:
            debug_str += "-norab"
        return debug_str

    def generate_user_embeddings(
        self,
        past_ids: paddle.Tensor,
        past_embeddings: paddle.Tensor,
        past_payloads: Dict[str, paddle.Tensor],
        delta_x_offsets: Optional[Tuple[paddle.Tensor, paddle.Tensor]] 
    ) -> paddle.Tensor:
        """
        [B, N] -> [B, N, D].
        """
        B, N, _ = past_embeddings.size()



    def forward(
        self,
        past_lengths: paddle.Tensor,
        past_ids: paddle.Tensor,
        past_embeddings: paddle.Tensor,
        past_payloads: Dict[str, paddle.Tensor]
    ) -> paddle.Tensor:
    """
        Runs the main encoder.

        Args:
            past_lengths: (B,) x int64
            past_ids: (B, N,) x int64 where the latest engaged ids come first. In
                particular, past_ids[i, past_lengths[i] - 1] should correspond to
                the latest engaged values.
            past_embeddings: (B, N, D) x float or (\sum_b N_b, D) x float.
            past_payloads: implementation-specific keyed tensors of shape (B, N, ...).

        Returns:
            encoded_embeddings of [B, N, D].
    """
    encoded_embeddings, _ = self.generate_user_embeddings(
            past_lengths=past_lengths,
            past_ids=past_ids,
            past_embeddings=past_embeddings,
            past_payloads=past_payloads,
        )
    return encoded_embeddings

