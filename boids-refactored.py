from matplotlib import pyplot as plt
from matplotlib import animation
import random
import yaml

plot_config = {
    "xlim": (-500, 1500),
    "ylim": (-500, 1500)
}


def get_boids():
    boid_x = [random.uniform(-450, 50) for x in range(50)]
    boid_y = [random.uniform(300, 600) for x in range(50)]
    boid_x_velocities = [random.uniform(0, 10) for x in range(50)]
    boid_y_velocities = [random.uniform(-20, 20) for x in range(50)]

    deltaXVs = [0] * len(boid_x)
    deltaYVs = [0] * len(boid_x)
    # Fly towards the middle
    for i in range(len(boid_x)):
        for j in range(len(boid_x)):
            deltaXVs[i] = deltaXVs[i] + ((boid_x[j] - boid_x[i] * 0.01) / len(boid_x))
            deltaYVs[i] = deltaYVs[i] + ((boid_y[j] - boid_y[i] * 0.01) / len(boid_x))

            # Fly away from nearby boids
            if (boid_x[j] - boid_x[i]) ** 2 + (boid_y[j] - boid_y[i]) ** 2 < 100:
                deltaXVs[i] = deltaXVs[i] + (boid_x[i] - boid_x[j])
                deltaYVs[i] = deltaYVs[i] + (boid_y[i] - boid_y[j])

            # Try to match speed with nearby boids
            if (boid_x[j] - boid_x[i]) ** 2 + (boid_y[j] - boid_y[i]) ** 2 < 10000:
                deltaXVs[i] = deltaXVs[i] + (boid_x_velocities[j] - boid_x_velocities[i]) * 0.125 / len(boid_x)
                deltaYVs[i] = deltaYVs[i] + (boid_y_velocities[j] - boid_y_velocities[i]) * 0.125 / len(boid_x)

        # Update velocities
        boid_x_velocities[i] = boid_x_velocities[i] + deltaXVs[i]
        boid_y_velocities[i] = boid_y_velocities[i] + deltaYVs[i]

        # Move according to velocities
        boid_x[i] = boid_x[i] + boid_x_velocities[i]
        boid_y[i] = boid_y[i] + boid_y_velocities[i]
    return boid_x, boid_y, boid_x_velocities, boid_y_velocities


def animate(boid_x, boid_y):
    figure = plt.figure()
    axes = plt.axes(xlim=plot_config["xlim"], ylim=plot_config["ylim"])
    scatter = axes.scatter(boid_x, boid_y)
    scatter.set_offsets(list(zip(boid_x, boid_y)))
    animation.FuncAnimation(figure, animate, frames=50, interval=50)
    plt.show()


def create_random_uniform_samples(lower_bound: int, upper_bound: int, number_of_samples: int):
    return [random.uniform(lower_bound, upper_bound) for _ in range(number_of_samples)]


def main():
    boid_x, boid_y, boid_x_velocity, boid_y_velocity = get_boids()
    animate(boid_x, boid_y)


if __name__ == "__main__":
    main()
