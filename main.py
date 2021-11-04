def drawZoro(self, logicalPosition):
        # logical_position = grid value on the board
        # grid_position = actual pixel values of the center of the grid
        logicalPositionArray = np.array(logicalPosition)
        gridPosition = self.convert_logical_to_grid_position(logicalPosition)
        self.canvas.create_oval(gridPosition[0] - symbolSize, gridPosition[1] - symbolSize,
                                gridPosition[0] + symbolSize, gridPosition[1] + symbolSize, width=symbolThickness,
                                outline=symbol_O_color)
