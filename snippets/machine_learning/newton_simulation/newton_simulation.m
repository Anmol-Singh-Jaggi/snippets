% Dummy statement to avoid writing function in the first line and making it a 'function file' instead of a 'script file'
1;


% The function to find zeroes of.
% The function is specifically chosen to not have any zeroes
% so as to show the weakness of Newton's method.
function y = f(x)
    y = (x - 5).^2 + 5;
endfunction


% The derivative of f(x)
function y = fd(x)
    y = 2 * (x - 5);
endfunction


% Initial guess
x0 = 1.5;

% Max number of iterations
itermax = 20;

% Epsilon value initialized to a very large value
eps = 1;

% A vector for storing the history of the approximate roots
xvals = x0;

% Number of iterations done
itercount = 0;

% Required for plotting f(x) vs x
x = linspace(0, 10, 100);

% Create a figure whose output is not rendered on the screen
% Not working currently; supposedly a bug in Octave
% A workaround is to use gnuplot instead of qt - `graphics_toolkit gnuplot`
% but this is very slow.
% Uncomment the following to activate the feature once the bug is fixed
% figure('Visible','off');

% The main loop
while eps >= 1e-5 && itercount <= itermax
    % x1 = New value of root
    % x0 = Current value of root
    x1 = x0 - f(x0) / fd(x0);

    % Plot f(x)
    % Plot a line passing through points [x0, f(x0)] and [x1, 0]
    % Plot a line passing through points [x1, 0] and [x1, f(x1)]
    % Plot a line passing through points [x0, 0] and [x0, f(x0)]
    plot(x, f(x), ";f(x);", [x0 x1], [f(x0) 0], "-r;f'(x);", [x1 x1], [0 f(x1)], ":r", [x0 x0], [0 f(x0)], ":r");
    title('f(x) = (x-5)^2 + 5');


    % Set limits for the axes shown in the plots
    xlim([0 10]);
    ylim([0 30]);

    % Label the two consecutive zeroes on the X-axis
    text(x0, -2, sprintf('x%d', itercount), 'color', 'red');
    text(x1, -2, sprintf('x%d', itercount+1), 'color', 'red');

    % Print the plot to a file
    filename = sprintf('output/%05d.jpg', itercount);
    print(filename)

    % Append the zero to the array of zeroes calculated so far
    xvals = [xvals; x1];

    % Calculate the epsilon value
    eps = abs(x1-x0);

    x0 = x1;
    itercount = itercount+1;
end


% Print the result of the iteration
xvals
f_zero = f(xvals(end))
eps
itercount

