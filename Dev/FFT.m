function varargout = FFT(varargin)
% FFT MATLAB code for FFT.fig
%      FFT, by itself, creates a new FFT or raises the existing
%      singleton*.
%
%      H = FFT returns the handle to a new FFT or the handle to
%      the existing singleton*.
%
%      FFT('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in FFT.M with the given input arguments.
%
%      FFT('Property','Value',...) creates a new FFT or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before FFT_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to FFT_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Author: Yiwen Feng

% Edit the above text to modify the response to help FFT

% Last Modified by GUIDE v2.5 01-Aug-2019 19:10:58

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @FFT_OpeningFcn, ...
                   'gui_OutputFcn',  @FFT_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before FFT is made visible.
function FFT_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to FFT (see VARARGIN)

% Choose default command line output for FFT
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes FFT wait for user response (see UIRESUME)
% uiwait(handles.figure1);

handles.popupmenu2.String = "Select Channel";
handles.popupmenu4.String = "Select Type";


% --- Outputs from this function are returned to the command line.
function varargout = FFT_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

global channel Fs filtered;
if any(isnan(Fs)) || isempty(Fs)
    Fs = str2double(inputdlg("Sampling Rate"));
end
if ~isempty(Fs) && ~isnan(Fs) && ~isempty(channel)
    f0 = 60; % Notch frequency
    fn = Fs/2; % Nyquist frequency
    freq_ratio = f0/fn; % ratio of Notch frequency to Nyquist frequency
    notch_width = f0/200;
    notch_zeros = [exp(sqrt(-1)*pi*freq_ratio), exp(-sqrt(-1)*pi*freq_ratio)];
    notch_poles = (1-notch_width)*notch_zeros;
    b = poly(notch_zeros); % get moving average filter coefficients
    a = poly(notch_poles); % get autoregressive filter coefficients
    filtered = filter(b, a, channel);
    axes(handles.axes1);
    x = 0: length(filtered)-1;
    plot(x, filtered);
    title("Time domain with 60Hz Notch filter");
    xlabel("Time");
    ylabel("Voltage");
    guidata(hObject, handles);
    handles.popupmenu4.String = {"Raw Data", "Filtered Data"};
else
    if any(isnan(Fs)) || isempty(Fs)
        msgbox("Invalid sampling rate", "Warning", "warn");
    else
        msgbox("No channel is selected", "Warning", "warn");
    end
    filtered = array2table(zeros(0));
end


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

global data;
[file, path] = uigetfile({"*.csv; *.txt", "Data File (*.csv; *.txt)"}, "Select Data File");
if ~isequal(file, 0)
    data = readtable(fullfile(path, file));
    handles.popupmenu4.String = {"Raw Data"};
else
    msgbox("No data file is selected", "Warning", "warn");
    data = array2table(zeros(0));
end
if ~isempty(data)
    data(:, any(ismissing(data))) = [];
    data = data(:, vartype("double"));
    handles.popupmenu2.String = data.Properties.VariableNames;
    msgbox("Data file is loaded", "Success", "help");
end


% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

global channel Fs filtered;
if any(isnan(Fs)) || isempty(Fs)
    Fs = str2double(inputdlg("Sampling Rate"));
end
if ~isempty(Fs) && ~isnan(Fs) && ~isempty(channel) && ~isempty(filtered)
    contents = cellstr(get(handles.popupmenu4, "String"));
    if ~isempty(filtered) && isequal(contents{get(handles.popupmenu4, "Value")}, "Filtered Data")
        use_data = filtered;
        plot_title = "Frequency domain with 60Hz Notch filter";
    elseif ~isempty(channel) && isequal(contents{get(handles.popupmenu4, "Value")}, "Raw Data")
        use_data = channel;
        plot_title = "Frequency domain";
    else
        msgbox("No available data", "Warning", "warn");
        return;
    end
    axes(handles.axes2);
    L = length(use_data); % length of signal
    y = fft(use_data);
    P2 = abs(y/L);
    P1 = P2(1: L/2+1);
    P1(2: end-1) = 2*P1(2: end-1);
    f = Fs*(0: (L/2))/L;
    plot(f, P1);
    title(plot_title);
    xlabel("Frequency (Hz)");
    ylabel("Amplitude");
    guidata(hObject, handles);
else
    if any(isnan(Fs)) || isempty(Fs)
        msgbox("Invalid sampling rate", "Warning", "warn");
    elseif isempty(channel)
        msgbox("No channel is selected", "Warning", "warn");
    else
        msgbox("No data file is selected", "Warning", "warn");
    end
end


% --- Executes on selection change in popupmenu2.
function popupmenu2_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns popupmenu2 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu2
global data channel;
if ~isempty(data)
    choice = get(handles.popupmenu2, "Value");
    channel = data{:, choice};
    axes(handles.axes1);
    x = 0: length(channel)-1;
    plot(x, channel);
    title("Time domain");
    xlabel("Time");
    ylabel("Voltage");
    guidata(hObject, handles);
else
    msgbox("No data file is selected", "Warning", "warn");
    channel = array2table(zeros(0));
end


% --- Executes during object creation, after setting all properties.
function popupmenu2_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on selection change in popupmenu4.
function popupmenu4_Callback(hObject, eventdata, handles)
% hObject    handle to popupmenu4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes during object creation, after setting all properties.
function popupmenu4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
