def patch_head():
    """
    print shape before head
    """
    import pandas as pd

    def head2(self):
        print(self.shape)
        return self.head1()

    pd.DataFrame.head1 = pd.DataFrame.head
    pd.DataFrame.head = head2
