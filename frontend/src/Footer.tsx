import {
  MDBFooter,
  MDBContainer,
  MDBRipple
} from 'mdb-react-ui-kit';

export default function Footer() {
  return (
    <MDBFooter className='text-center text-white' style={{ backgroundColor: '#ffff' }}>
      <MDBContainer className='p-4'>
        <section className=''>
          <div className='d-flex justify-content-center'>
            <MDBRipple
              rippleColor='light'
              className='bg-image hover-overlay shadow-1-strong rounded'
            >
              <a href="https://www.spaceappschallenge.org">
              <img src="space_apps.png.webp" width="200" height="200" alt="Logo" />
              </a>

              <a href='#!'>
                <div
                  className='mask'
                  style={{ backgroundColor: 'rgba(251, 251, 251, 0.2)' }}
                ></div>
              </a>
            </MDBRipple>
          </div>
        </section>
        
      </MDBContainer>

      <div className='text-center p-3' style={{ backgroundColor: 'rgba(0, 0, 0, 0.2)' }}>
        © 2023 Copyright: 
        <a className='text-white' >
           TeamFES
        </a>
      </div>
    </MDBFooter>
  );
}
