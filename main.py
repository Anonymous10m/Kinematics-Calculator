t_range = np.arange(0,unit_sec(t) + 0.1, 0.1)
        acc = [a]*len(t_range)
        v = [(float(u) + float(a)*float(unit_sec(t))) for t in t_range]
        s = [(float(u)*float(unit_sec(t)) + 0.5*float(a)*float(unit_sec(t))**2) for t in t_range]
        
        ax1.plot(t_range,acc, label = "Acceleration")
        ax2.plot(t_range,v, 'orange', label = "Velocity")
        ax3.plot(t_range,s, 'green', label = "Distance")

        ax1.set_title('Acceleration(m\s^2) v/s Time(s)')
        ax1.set_xlabel('Time(s)')
        ax1.set_ylabel('Acceleration(m/s^2)')


        ax2.set_title('Velocity(m/s) v/s Time(s)')
        ax2.set_xlabel('Time(s)')
        ax2.set_ylabel('Velocity(m/s)')

        ax3.set_title('Distance(m) v/s Time(s)')
        ax3.set_xlabel('Time(s)')
        ax3.set_ylabel('Distance(m)')

        ax1.grid()
        ax2.grid()
        ax3.grid()

        ax1.legend(loc = 'upper left')
        ax2.legend(loc = 'upper left')
        ax3.legend(loc = 'upper left')

        plt.subplots_adjust(hspace=0.6)
        fig.suptitle("Graphs of the Given Motion")
        plt.show()
