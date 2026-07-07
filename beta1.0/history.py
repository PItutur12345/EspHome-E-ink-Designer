import copy



class HistoryManager:



    def __init__(self):


        self.undo_stack = []

        self.redo_stack = []





    def save(

        self,

        objects

    ):


        self.undo_stack.append(

            copy.deepcopy(objects)

        )


        self.redo_stack.clear()





    def undo(

        self,

        current

    ):


        if not self.undo_stack:

            return None



        self.redo_stack.append(

            copy.deepcopy(current)

        )


        return self.undo_stack.pop()





    def redo(

        self,

        current

    ):


        if not self.redo_stack:

            return None



        self.undo_stack.append(

            copy.deepcopy(current)

        )


        return self.redo_stack.pop()





    def can_undo(self):


        return len(

            self.undo_stack

        ) > 0





    def can_redo(self):


        return len(

            self.redo_stack

        ) > 0
