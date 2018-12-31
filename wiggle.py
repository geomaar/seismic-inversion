def wiggle(seismic, time=None, offset=None, sc=1, ornt='d'):
    """
    Plots a shaded wiggle plot 

    Args:
        seismic: matrix of waveform columns
        time: time axis vector
        offset: space axis vector


    %   wiggle(seismic,t,z,mag)   - scales waveforms by given magnification
    %   wiggle(seismic,t,z,m,'a') - changes time axis orientation to 'across'
    %
    %   WIGGLE returns handle to created graphics objects, so that
    %   set(wiggle(x,t,z), 'face',c1, 'edge',c2') will specify colours,
    %   and scale factor used

    """

    n, m = seismic.shape
    n1 = range(n, 0, -1)
    if time is None:
        time = range(1, n+1)
    if offset is None:
        offset = range(1, m+1)

    colour = 'k'
    % default colour
    offset = offset(: )'
    %
    scale = (2*mean(diff(offset))) * (sc / max(max(seismic) - min(seismic)))
    if sc < 0, scale = -sc
    end
    seismic = seismic * scale
    %

    if ornt == 'd'
    h = fill(offset(ones(2*n, 1), :)+[seismic
                                       min(seismic(n1, :), 0)], time([1:n n1]), colour)
    set(h, 'EdgeColor', colour),
    set(gca, 'Ydir', 'r')
    dz = offset(2)-offset(1)
    axis([min(offset)-dz max(offset)+dz min(time) max(time)])
    else
    h = fill(time([1:n n1]), offset(ones(2*n, 1), :)-[seismic
                                                       min(seismic(n1, :), 0)], colour)
    ...
    set(h, 'EdgeColor', colour), set(gca, 'Ydir', 'r')
    end

    %
    if nargout > 0, handle = h
    end
    %
