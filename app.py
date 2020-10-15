import glob
import streamlit as st
import plotly.graph_objects as go
from flowtracks.io import iter_trajectories_ptvis


# project_title = st.sidebar.text_input(label="Title of Project",
#                                       value="3D trajectories")

# st.title(project_title)

path = st.text_input('Insert folder path, including /res', '/home/user/Downloads/test_cavity/res/')
if path:
    ptv_list = sorted(glob.glob(path+'/ptv_is.*'))

# st.text(ptv_list)

st.text("There are files in the range")
st.text(ptv_list[0].rsplit('/')[-1])
st.text(ptv_list[-1].rsplit('/')[-1])

st.text("Choose first, last:")
first = int(st.text_input('first', 10001))
last = int(st.text_input('last', 10004))

st.text("Choose minimum length")
min_length = int(st.text_input("minimum length:",last-first))
# min_length = st.slider("min_length",0, last-first-1)

traj = iter_trajectories_ptvis(path+'ptv_is.%d', first=first,
                            last=last, traj_min_len=min_length)


data = []

for t in traj:
    data.append(go.Scatter3d(x=t.pos()[:, 0], y=t.pos()[:, 1], z=t.pos()[:, 2],
                             mode='lines'))



# print(np.array(x))

# x = np.vstack(x)
# y = np.vstack(y)
# z = np.vstack(z)


fig = go.Figure(data=data)



# st.text(data)

fig.update_layout(title='Trajectories', autosize=True,
                  width=800, height=800,
                  margin=dict(l=40, r=40, b=40, t=40),
                  showlegend=False)


st.plotly_chart(fig)
