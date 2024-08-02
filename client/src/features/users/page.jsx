import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { DataGrid } from '@mui/x-data-grid';
import { Button, Container, Typography, Grid } from '@mui/material';
import { Edit, Delete } from '@mui/icons-material';
import { fetchUsers } from '../userSlice';
import Dialog from '@mui/material/Dialog';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import EditForm from './editForm';



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
  const [isEdit, setIsEdit] = React.useState(false);
  const [userDetails,setUserDetails] = React.useState()
  const dispatch = useDispatch();
  const users = useSelector((state) => state.user.users);



  const handleClickOpen = (details) => {
    setOpen(true);
    setIsEdit(true);
    setUserDetails(details)
  };

  const handleClose = () => {
    setOpen(false);
  };
  

  useEffect(() => {
    dispatch(fetchUsers(USERS));
    // dispatch(getUsers());
  }, [dispatch]);

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
          >
          </Button>
          <Button
            startIcon={<Delete />}
            color="secondary"
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
            <Button  variant='contained' onClick={() => {
              setOpen(true)
            }}>Add User</Button>
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
        <DialogTitle>{isEdit ? 'Edit User' : 'Add User'}</DialogTitle>
        <DialogContent>      
            <EditForm userDetails={userDetails} onClose={handleClose} isEdit={isEdit} onSetEdit={setIsEdit}/>   
        </DialogContent>
      </Dialog>
    </Container>
  );
};

export default UsersPage;