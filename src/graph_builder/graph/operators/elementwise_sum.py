from typing import Dict

from graph_builder.graph.graph import Operator, Variable
from graph_builder.graph.operators import attributes as A


class ElementwiseSum(Operator):
    """
    n入力を加算するレイヤー
    """
    attributes = {A.PostElementwise,
                  A.PostChannelwise,
                  A.FirstInplace}

    def __init__(self, name: str, parameters: Dict[str, object] = None):
        """
        parameters: {n_inputs: int}
        n_inputs: 入力変数の数
        :param name: 
        :param parameters: 
        """
        super().__init__(name, parameters)

    def __call__(self, *xs: Variable):
        y = Variable(xs[0].shape)
        for x in xs:
            self.append_input("x", x)
        self.append_output("y", y)
        return y,
