class moveItems:

    def moveUp(listBox):
        # get where they are in the listbox
        index = listBox.curselection()
        # check if there's nothing
        if not index:
            return
        else:
            for pos in index:
                # check if they are at the top of the listbox
                if pos == 0:
                    # could use return here since I am using a single selection listBox, but this keeps it open for multi-selection
                    continue
                # get the text associated with where they are at
                text = listBox.get(pos)
                # delete the spot where they are and "move" the selected text up
                listBox.delete(pos)
                listBox.insert(pos - 1, text)
                # set their selected text as the one they just moved up
                listBox.selection_set(pos - 1)
    
    def moveDown(listBox):
        # get where they are in the listbox
        index = listBox.curselection()
        # this would be the bottom of the listbox
        lastIndex = listBox.size() - 1

        # check for nothing
        if not index:
            return
        else:
            for pos in index:
                # check if they are at the bottom
                if pos == lastIndex:
                    # could use return here since I am using a single selection listBox, but this keeps it open for multi-selection
                    continue
                # get the text associated with where they are
                text = listBox.get(pos)
                # delete the spot where they are and "move" it down 1 position
                listBox.delete(pos)
                listBox.insert(pos + 1, text)
                # set their selected text as the one they just moved down
                listBox.selection_set(pos + 1)
                