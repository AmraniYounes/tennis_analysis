import numpy as np

def predict_ball_position(ball_positions, minimap_width, minimap_height):
    """Predict the next ball position based on the last two positions."""
    if len(ball_positions) >= 2:
        (x1, y1) = ball_positions[-2]
        (x2, y2) = ball_positions[-1]
        
        v_x = x2 - x1
        v_y = y2 - y1
        
        x_pred = x2 + v_x
        y_pred = y2 + v_y

        x_pred = np.clip(x_pred, 0, minimap_width - 1)
        y_pred = np.clip(y_pred, 0, minimap_height - 1)

        return x_pred, y_pred
    return None