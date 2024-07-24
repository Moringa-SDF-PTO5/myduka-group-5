import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { DataGrid } from '@mui/x-data-grid';
import { Button, Container, Typography, Grid } from '@mui/material';
import { Edit, Delete } from '@mui/icons-material';
import { fetchUsers } from '../userSlice';
// import { fetchUsers, getUsers } from '../userSlice';
import Dialog from '@mui/material/Dialog';
import DialogContent from '@mui/material/DialogContent';
// import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import EditForm from './editForm';
// import { fetchUsers, addUser, editUser, deleteUser } from '../../actions/userActions';

const USERS= [
    {
      id: 1,
      name: 'Winnie',
      email: 'winnie.abuor@student.moringaschool.com',
      role: 'Clerk',
      active: true,
    },
    {
      id: 2,
      name: 'Josephine',
      email: 'josephine.nzioka1@student.moringaschool.com',
      role: 'Clerk',
      active: false,
    },
  ]

const UsersPage = () => {
  const [open, setOpen] = React.useState(false);
  const [userDetails,setUserDetails] = React.useState()
  const dispatch = useDispatch();
  const users = useSelector((state) => state.user.users);


  const handleClickOpen = (details) => {
    setOpen(true);
    setUserDetails(details)
  };

  const handleClose = () => {
    setOpen(false);
  };

  useEffect(() => {
    dispatch(fetchUsers(USERS));
    // dispatch(getUsers());
  }, [dispatch]);

//   const handleEdit = (id) => {
//     console.log('Edit user', id);
//     dispatch(editUser({ id, name: 'Updated Name', email: 'updated.email@example.com' }));
//   };

//   const handleDelete = (id) => {
//     dispatch(deleteUser(id));
//   };

  const columns = [
    { field: 'name', headerName: 'Name', flex: 1 },
    { field: 'email', headerName: 'Email', flex: 1 },
    { field: 'role', headerName: 'Role', flex: 1 },
    { field: 'active', headerName: 'Active', type: 'boolean', flex: 1 },
    {
      field: 'actions',
      headerName: 'Actions',
      flex: 1,
      renderCell: (params) => {
        
        return(
        <div>
          <Button
            startIcon={<Edit />}
            color="primary"
            onClick = {() => handleClickOpen(params.row)}
            // onClick={() => handleEdit(params.row.id)}
          >
          </Button>
          <Button
            startIcon={<Delete />}
            color="secondary"
            // onClick={() => handleDelete(params.row.id)}
          >
          </Button>
        </div>
        )
        },
    },
  ];

  return (
    <Container maxWidth="lg">
        <div className='flex items-center space-x-64'>
            <Typography variant="h4" component="h1" gutterBottom>
                Manage Clerks
            </Typography>
            <Button className="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 my-2 border border-gray-400 rounded shadow">
                Add User
            </Button>
      </div>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <div style={{ height: 400, width: '100%' }}>
            <DataGrid
              rows={users}
              columns={columns}
              pageSize={5}
              rowsPerPageOptions={[5]}
              disableSelectionOnClick
            />
          </div>
        </Grid>
      </Grid>
      <Dialog
        open={open}
        onClose={handleClose}
      >
        <DialogTitle>Edit User</DialogTitle>
        <DialogContent>      
            <EditForm userDetails={userDetails}/>   
        </DialogContent>
      </Dialog>
    </Container>
  );
};

export default UsersPage;